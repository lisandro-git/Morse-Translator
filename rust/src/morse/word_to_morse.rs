use super::*;

pub fn encode(word: String) -> Vec<String>{
    let morse_signs = alphabet::ConfigSerde::read_config().unwrap();
    let categories: Vec<String> = vec![
        "alphabet".to_string(),
        "number".to_string(),
        "special".to_string(),
        "prosigns".to_string(),
    ];

    let (alphabet_key, alphabet_value) = morse_signs.get_key_value("alphabet").unwrap();
    let (number_key, number_value) = morse_signs.get_key_value("number").unwrap();
    let (special_key, special_value) = morse_signs.get_key_value("special").unwrap();
    let (prosigns_key, prosigns_value) = morse_signs.get_key_value("prosigns").unwrap();

    return vec![];
}
