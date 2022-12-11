use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Request, Response, Server};
use local_ip_address::local_ip;
use mysql::params;
use mysql::prelude::Queryable;
use std::convert::Infallible;
use std::net::SocketAddr;
use unwrap_or::unwrap_some_or;

const SQL_PASSWORD: &'static str = "JA4eRQhwizvMB69VA2UgXu5iP9KsgatvsCxnExjyBy3em";
const SQL_USERNAME: &'static str = "sensor_one";
const SQL_HOST: &'static str = "billenius.com";
const SQL_TABLE: &'static str = "termoster";
const SQL_PORT: u16 = 3306;

#[tokio::main]
async fn main() {
    // mysql

    // We'll bind to 127.0.0.1:3000
    let addr = SocketAddr::from(([0, 0, 0, 0], 8579));

    // A `Service` is needed for every connection, so this
    // creates one from our `hello_world` function.
    let make_svc = make_service_fn(|_conn| async {
        // service_fn converts our function into a `Service`
        Ok::<_, Infallible>(service_fn(handle))
    });

    let server = Server::bind(&addr).serve(make_svc);

    // Get local ip, if possible or else nevermind
    let local_ip_address = local_ip()
        .and_then(|ipaddr| Ok(ipaddr.to_string()))
        .unwrap_or_default();
    println!(
        "Listening on port {} (local ip: {})",
        addr.port(),
        local_ip_address
    );

    // Run this server for... forever!
    if let Err(e) = server.await {
        eprintln!("server error: {}", e);
    }
}

async fn handle(req: Request<Body>) -> Result<Response<Body>, Infallible> {
    let headers = req.headers();

    let pass_match = unwrap_some_or!(
        headers.get("x-password"),
        return Ok(Response::new("No password".into()))
    ) == SQL_PASSWORD;
    if !pass_match {
        return Ok(Response::new("Password is incorrect".into()));
    }

    let sql_url = format!(
        "mysql://{}:{}@{}:{}/{}",
        &SQL_USERNAME, &SQL_PASSWORD, &SQL_HOST, &SQL_PORT, &SQL_TABLE
    );

    let mut mysql_conn = mysql::Conn::new(sql_url.as_str()).unwrap();
    let mut s = String::new();

    if headers.contains_key("x-celsius") && headers.contains_key("x-humidity") {
        if let Err(e) = mysql_conn.exec_drop(
            r"INSERT INTO meassures (celsius, humidity) VALUES (:celsius, :humidity)",
            params! {
                "celsius"=>headers["x-celsius"].to_str().unwrap(),
                "humidity"=>headers["x-humidity"].to_str().unwrap(),
            },
        ) {
            s.push_str(&e.to_string());
            eprintln!("{:?}", e);
        }
    }

    Ok(Response::new(if s.is_empty() {
        "Success".into()
    } else {
        s.into()
    }))
}
