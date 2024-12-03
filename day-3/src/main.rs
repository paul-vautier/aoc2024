use pepser::{
    impls::{eof, sequence, take_while},
    traits::{discard, drop_until, wrapped, Input, ParseResult, Parser},
};
const FILE_CONTENT: &str = include_str!("input.txt");
fn main() {
    let content: String = String::from(FILE_CONTENT);
    let muls = parse_first(content.as_str()).unwrap().1;

    println!("{:?}", muls.into_iter().fold(0, |sum, (a, b)| sum + a * b));

    let muls = parse_second(content.as_str()).unwrap().1;

    println!("{:?}", muls.into_iter().fold(0, |sum, (a, b)| sum + a * b))
}

fn mul<'a>() -> impl Parser<&'a str, Output = (i32, i32)> {
    wrapped(
        sequence("mul("),
        digit().and(discard(sequence(","), digit())),
        sequence(")"),
    )
}
fn digit<'a>() -> impl Parser<&'a str, Output = i32> {
    take_while(|c| c.is_digit(10))
        .map(str::parse::<i32>)
        .map(Result::unwrap)
}

fn parse_first<'a>(input: &'a str) -> ParseResult<&'a str, Vec<(i32, i32)>> {
    return drop_until(mul()).many().parse(input);
}

fn parse_second<'a>(input: &'a str) -> ParseResult<&'a str, Vec<(i32, i32)>> {
    return drop_until(
        mul().map(|tuple| Some(tuple)).or(sequence("don't()")
            .and(drop_until(sequence("do()").map(|_| ()).or(eof())))
            .map(|_| None)),
    )
    .many()
    .map(|vecs| vecs.into_iter().flatten().collect::<Vec<(i32, i32)>>())
    .parse(input);
}
