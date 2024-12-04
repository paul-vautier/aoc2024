use std::str::Chars;

const FILE_CONTENT: &str = include_str!("test.txt");
const DIRECTION: [(i32, i32); 8] = [
    (1, 0),
    (0, 1),
    (1, 1),
    (1, -1),
    (-1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1),
];
const MAS: [char; 4] = ['X', 'M', 'A', 'S'];
fn main() {
    let chars = FILE_CONTENT
        .lines()
        .map(str::chars)
        .map(Chars::collect::<Vec<char>>)
        .collect::<Vec<Vec<char>>>();
    println!("{}", solve_first(chars.clone()));
    println!("{}", solve_second(chars));
}

fn solve_first(chars: Vec<Vec<char>>) -> u32 {
    let mut xmas_cnt = 0;

    for i in 0..chars.len() {
        for j in 0..chars[i].len() {
            for (dx, dy) in DIRECTION {
                if MAS.iter().enumerate().all(|(curr_idx, curr)| {
                    let x = i as i32 + dx * curr_idx as i32;
                    let y = j as i32 + dy * curr_idx as i32;
                    x < chars.len() as i32
                        && x >= 0
                        && y < chars[i].len() as i32
                        && y >= 0
                        && *curr == chars[x as usize][y as usize]
                }) {
                    xmas_cnt += 1;
                }
            }
        }
    }

    xmas_cnt
}

fn solve_second(chars: Vec<Vec<char>>) -> u32 {
    let mut xmas_cnt = 0;
    for i in 1..chars.len() - 1 {
        for j in 1..chars[i].len() - 1 {
            if chars[i][j] == 'A' {
                if (chars[i - 1][j - 1] == 'M' && chars[i + 1][j + 1] == 'S'
                    || chars[i - 1][j - 1] == 'S' && chars[i + 1][j + 1] == 'M')
                    && (chars[i - 1][j + 1] == 'M' && chars[i + 1][j - 1] == 'S'
                        || chars[i - 1][j + 1] == 'S' && chars[i + 1][j - 1] == 'M')
                {
                    xmas_cnt += 1;
                }
            }
        }
    }
    xmas_cnt
}
