def test(num):
    if num >= 3:
        print("room is crowded")
list = ["marco", "pranav", "james", "zain"]
test(len(list))
list.remove("zain")
list.remove("james")
test(len(list))