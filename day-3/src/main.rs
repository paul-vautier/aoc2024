use pepser::{
    errors::{ErrorSource, ParserError},
    impls::{any, none_of, not, sequence, take_while, ws},
    traits::{discard, opt, parse_if, sep_by, value, wrapped, ParseResult, Parser},
};
const FILE_CONTENT: &str = include_str!("input.txt");
fn main() {
    let content: String = String::from(FILE_CONTENT);
    let muls = parse(content.as_str()).unwrap().1;

    println!("{:?}", muls);
    println!("{:?}", muls.into_iter().fold(0, |sum, (a, b)| sum + a * b))
}

fn digit<'a>() -> impl Parser<&'a str, Output = i32> {
    take_while(|c| c.is_digit(10))
        .map(str::parse::<i32>)
        .map(Result::unwrap)
}
fn parse<'a>(input: &'a str) -> ParseResult<&'a str, Vec<(i32, i32)>> {
    return mul()
        .or(take_any().map(|_| Vec::<(i32, i32)>::new()))
        .many()
        .map(|vecs| vecs.into_iter().flatten().collect::<Vec<(i32, i32)>>())
        .parse(input);
}

fn mul<'a>() -> impl Parser<&'a str, Output = Vec<(i32, i32)>> {
    return wrapped(
        sequence("mul("),
        digit().and(discard(sequence(","), digit())),
        sequence(")"),
    )
    .map(|tuple| vec![tuple]);
}
fn take_any<'a>() -> impl Parser<&'a str, Output = &'a str> {
    return |input| {
        let mut seen: bool = true;
        return take_while(move |c| {
            if (seen) {
                seen = false;
                return true;
            }
            return false;
        })
        .parse(input);
    };
}
