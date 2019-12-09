for i in [1, 1.2, "qwerty", [1, '2'], {"key_1": 1, "key_2": "ytrewq"},
          Exception, complex(5, 6), (1, "col_1"), False, None, b'test', bytearray(b'test1')]:
    print(f"Type of element {i} is {type(i)}")
