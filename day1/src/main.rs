use std::fs::File;
use std::io::{prelude::*, BufReader};

fn main() {
    // Read input.txt
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    // Aux is the accumulator for each elf
    let mut aux: u32 = 0;
    let mut max: [u32; 3] = [0, 0, 0];
    // For each line
    for line in reader.lines() {
        let l: String = line.unwrap();
        // If line is empty, new elf
        if l.is_empty() {
            max.sort();
            // Loop through max
            for i in 0..max.len() {
                if aux > max[i] {
                    max[i] = aux;
                    break;
                }
            }
            aux = 0;
            continue;
        }

        let calories: u32 = l.parse().unwrap();
        aux += calories;
    }

    let sum: u32 = max.iter().sum();
    println!("The top three elves carrying most calories are carrying {} calories in total", sum);
}
