use std::fs::File;
use std::io::{prelude::*, BufReader};
use std::collections::HashMap;

fn main() {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

   // More complex data structure, more efficient, less complex code
   // char: encrypted, wins
   let rule = HashMap::from([
        ("A", ["X", "Y", "Z"]), // rock
        ("B", ["Y", "Z", "X"]), // paper
        ("C", ["Z", "X", "Y"])  // scissors
    ]);

    let points= HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3)
    ]);

    let (mut sum_one, mut sum_two): (u32, u32) = (0, 0);
    for line in reader.lines() {
        let l: String = line.unwrap();
        let (input, answer) = (&l[0..1], &l[2..3]);
        let r = rule.get(input).unwrap();
        // The score of what you chose
        sum_one += points.get(answer).unwrap();
        // Part two
        // I need to lose
        if answer == "X" {
            sum_two += points.get(r[2]).unwrap();
        }
        // I need a draw
        else if answer == "Y" {
            sum_two += points.get(r[0]).unwrap() + 3;
        }
        // I need a win
        else if answer == "Z" {
            sum_two += points.get(r[1]).unwrap() + 6;
        }
        // Draw
        if answer == r[0] {
            sum_one += 3;
            continue;
        }
        // Win
        if answer == r[1] {
            sum_one += 6;
        }
    }

    println!("Total score, part one: {}", sum_one);
    println!("Total score, part two: {}", sum_two);
}
