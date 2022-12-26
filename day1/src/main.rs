use std::fs::File;
use std::io::{prelude::*, BufReader};

fn main() {
    // Read input.txt
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    // Aux is the accumulator for each elf
    let (mut aux, mut max) : (u32, u32) = (0, 0);
    // For each line
    for line in reader.lines() {
        let l: String = line.unwrap();
        // If line is empty, new elf
        if l.is_empty() {
            if aux > max {
                max = aux;
            }
            aux = 0;
            continue;
        }

        let calories: u32 = l.parse().unwrap();
        aux += calories;
    }

    println!("The elf with most calories is carrying {} calories.", max);
}
