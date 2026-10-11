
# תרגיל 1
def inventory_summary(dic):

    count = 0
    for k  in dic:
        count = count + (dic[k][0])

    return  count


print(inventory_summary({"milk":(2,3), "bread":(3,5)}))

# תרגיל 2
def print_args_kwargs(*args, **kwargs):
    for a in args:
        print(*args)
    for k , v in kwargs.items():
        print(k, v)

print_args_kwargs(2,3,6,8 , milk=1, bread=2)