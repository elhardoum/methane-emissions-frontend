# Tauri app

Tauri is a framework for building cross-platform desktop (and mobile) applications with web technologies (HTML, CSS, and JavaScript). It is similar to Electron, but with a smaller footprint and a more secure runtime.

## Dependencies

* [Tauri](https://tauri.app/v1/guides/getting-started/prerequisites)

> Tauri installation process includes installation of `rust`.

After that you can install `tauri-cli` and `cargo-make`:

```console
rustup update
cargo install tauri-cli
cargo install cargo-make
```

## Build

```console
cargo make built-tauri
```

## Limitations

At the moment, the Tauri app does not add any functionality to the frontend. It is just a wrapper around it. However, if we manage to cross-compile H5 Keras model for the target or build the Tauri app on the target architecture, we will be able to ship the app with the model and run it without the need for the web app.
