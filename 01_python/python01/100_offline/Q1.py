# Keyword Arguments
def greet(name, age, greeting="Hello"):
    print(f"안녕하세요, {name}님! {age}살이시군요. {greeting}!")
# greet("Dave", "Hello", age=35) -> 에러 발생!! TypeError: greet() got multiple values for argument 'age'
greet("Dave", greeting="Hello", age=35)  # age와 greeting의 순서를 바꿔도 동작함