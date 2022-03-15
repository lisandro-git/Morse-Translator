use std::fs;
use std::error::Error;
use serde_json::{Value, Map};

pub struct ConfigSerde;

impl ConfigSerde {
    pub fn read_config() -> Result<Map<String, Value>, Box<Error>> {
        let config = fs::read_to_string("src/morse_code.json")?;
        let parsed: Value = serde_json::from_str(&config)?;
        let obj: Map<String, Value> = parsed.as_object().unwrap().clone();
        Ok(obj)
    }
}