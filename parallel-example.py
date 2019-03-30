import multiprocessing as mp
import random
import string

random.seed(123)

output = mp.Queue()


def rand_string(length, output):
    rand_str = ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits)
        for i in range(length))
    output.put(rand_str)


if __name__ == "__main__":
    mp.pool.Pool().appl
    processes = [mp.Process(target=rand_string, args=(5, output))
                 for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]

    print(results)
