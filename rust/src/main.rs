pub mod morse;


fn main() {
        let encoded = morse::word_to_morse::encode(String::from("Hello how are you ?"));
    println!("{}", encoded);
    let decoded = morse::morse_to_word::decode(encoded);
    println!("{}", decoded);
}
