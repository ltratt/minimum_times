use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

use sha2::{Digest, Sha256};

fn main() {
    let mut words = HashMap::new();
    let f = File::open("/usr/share/dict/words").unwrap();
    for l in BufReader::new(f).lines().map(|l| l.unwrap()) {
        words.insert(Sha256::digest(l.as_bytes()), l);
    }

    for _ in 0..1000 {
        for (_, v) in &words {
            if v == "zygote" {
                break;
            }
        }
    }
}
