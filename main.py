
from assets.prompts import behaviors

def main() -> None:
	test_str_0: str = "Hallo {var}"  # {name} gets formatted with string.format(var="asdfas")
	test_str_1: str = "Welt"

	print(test_str_0.format(var=test_str_1))
	behaviors.formal(1)



if __name__ == '__main__':
    main()
