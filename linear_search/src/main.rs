use std::fs::File;
use std::io::{BufRead, BufReader};

use rand::thread_rng;
use rand::seq::SliceRandom;

fn main() {
    let mut words = Vec::new();
    let f = File::open("/usr/share/dict/words").unwrap();
    for l in BufReader::new(f).lines() {
        words.push(l.unwrap())
    }

    let choice = words.choose(&mut thread_rng()).unwrap();
    for _ in 0..10000 {
        assert!(words.iter().any(|w| w == choice));
    }
}
