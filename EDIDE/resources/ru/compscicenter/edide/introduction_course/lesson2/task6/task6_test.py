from test_helper import run_common_tests, import_file


def test_value(path):
    file = import_file(path)
    if not file.is_equal:
        return "#study_plugin test OK"
    return "#study_plugin Please, reload the task and try again."



if __name__ == '__main__':
    run_common_tests('''two = 2
three = 3

is_equal = two operator three
''', '''two = 2
three = 3

is_equal = two  three
''', "You should modify the file")

    # TODO: get filepath. Let's now assume that we pass it as the last item in command-line
    import sys
    path = sys.argv[-1]
    print(test_value(path))