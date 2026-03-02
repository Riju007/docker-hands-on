use axum::{Router, routing::get};
use serde_json::json;
use tracing::{info};
use tracing_subscriber::FmtSubscriber;

async fn health() -> String {
    println!(
        "{}",
        serde_json::json!({
            "service": "rust",
            "level": "info",
            "message": "health check called"
        })
    );
    json!({"service": "rust", "status": "ok"}).to_string()
}

async fn info() -> String {
    let info_dict = json!({"language": "rust"});
    return info_dict.to_string();
}

#[tokio::main]
async fn main() {
    // initialize tracing
    // tracing_subscriber::fmt::init();
    let subscriber = FmtSubscriber::builder().finish();
    tracing::subscriber::set_global_default(subscriber).expect("setting default subscriber failed");
    info!(service = "rust", message = "Server started");
    let app = Router::new()
        .route("/health", get(health))
        .route("/info", get(info));

    // run our app with hyper, listening globally on port 3000
    let listener = tokio::net::TcpListener::bind("0.0.0.0:4000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
