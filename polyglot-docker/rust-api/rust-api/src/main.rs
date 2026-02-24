use axum::{Router, routing::get};
use serde_json::json;

async fn health() -> String {
    json!({"service": "rust", "status": "ok"}).to_string()
}

async fn info() -> String {
    let info_dict = json!({"language": "rust"});
    return info_dict.to_string();
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/health", get(health))
        .route("info", get(info));

    axum::Server::bind(&"")
}