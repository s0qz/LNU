use hyper::{Body, Method, Request, Response};
use mysql::params;
use mysql::prelude::Queryable;
use serde::Serialize;
use std::convert::Infallible;
use unwrap_or::unwrap_some_or;

const SQL_PASSWORD: &'static str = "JA4eRQhwizvMB69VA2UgXu5iP9KsgatvsCxnExjyBy3em";
const SQL_USERNAME: &'static str = "sensor_one";
const SQL_HOST: &'static str = "billenius.com";
const SQL_TABLE: &'static str = "termoster";
const SQL_PORT: u16 = 3306;

#[derive(Serialize, Debug)]
struct SQLEntry {
    created_at: String,
    celsius: f64,
    humidity: f64,
}

fn query_to_parts(query: &str) -> Vec<(String, String)> {
    let normalized_str = query.replace("?", "\u{2122}").replace("&", "\u{2122}");
    normalized_str
        .split("\u{2122}")
        .map(|pair| {
            let mut p = pair.split("=");
            (p.next().unwrap().to_string(), p.next().unwrap().to_string())
        })
        .collect::<Vec<(String, String)>>()
}

fn get_date_part(parts: Vec<(String, String)>) -> Option<String> {
    for part in parts {
        if part.0 == "since-date" {
            return Some(part.1);
        }
    }
    None
}

pub async fn handle(req: Request<Body>) -> Result<Response<Body>, Infallible> {
    let headers = req.headers();

    let sql_url = format!(
        "mysql://{}:{}@{}:{}/{}",
        &SQL_USERNAME, &SQL_PASSWORD, &SQL_HOST, &SQL_PORT, &SQL_TABLE
    );
    let mut mysql_conn = mysql::Conn::new(sql_url.as_str()).unwrap();
    let mut s = String::new();

    if req.method() == Method::POST {
        // Check for password
        let pass_match = unwrap_some_or!(
            headers.get("x-password"),
            return Ok(Response::new("No password".into()))
        ) == SQL_PASSWORD;
        if !pass_match {
            return Ok(Response::new("Password is incorrect".into()));
        }

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
    } else {
        let parts = query_to_parts(req.uri().query().unwrap());

        let date = if let Some(date) = get_date_part(parts) {
            date
        } else if headers.contains_key("x-since-date") {
            headers["x-since-date"].to_str().unwrap().to_string()
        } else {
            return Ok(Response::new("No date".into()));
        };

        let query: Vec<(String, String, String)> = match mysql_conn.query(format!(
            "SELECT created_at, celsius, humidity  FROM meassures WHERE created_at > '{}'",
            date
        )) {
            Ok(k) => k,
            Err(e) => return Ok(Response::new(format!("{:?}", e).into())),
        };

        let mut entries: Vec<SQLEntry> = Vec::new();
        for (date, cel, hum) in query.iter() {
            entries.push(SQLEntry {
                created_at: date.clone(),
                celsius: cel.trim().parse().expect("Kunde inte parsea celsius"),
                humidity: hum.trim().parse().expect("Kunde inte parsea humidity"),
            })
        }

        s = serde_json::to_string(&entries).unwrap();
    }

    Ok(Response::new(if s.is_empty() {
        "Success".into()
    } else {
        s.into()
    }))
}
