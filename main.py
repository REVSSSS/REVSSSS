from time import sleep, perf_counter

def task():
    print('Choosing a task to perform.....')
    sleep(1)
    print('Nothing')

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} Second(s) to complete.')
