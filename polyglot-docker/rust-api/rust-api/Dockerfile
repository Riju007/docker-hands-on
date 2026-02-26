# Builder
FROM rust:1.93 AS builder

WORKDIR /app

COPY . /app

RUN cargo build --release

# Runtime
FROM debian:bookworm-slim

WORKDIR /app

COPY --from=builder /app/target/release/rust-api /app

EXPOSE 4000

CMD ["./rust-api"]