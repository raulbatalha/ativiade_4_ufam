from src.hello_task import HelloTask
from src.producer import Producer
from src.bike_computer import BikeComputer

def main():
    # Criando e executando HelloTask
    task_a = HelloTask("A", amount=5, delay_time=0.5)
    task_b = HelloTask("B", amount=7, delay_time=0.5)
    task_a.start()
    task_b.start()
    task_a.join()
    task_b.join()

    # Criando e executando Producer
    producer_a = Producer(char="A", repetitions=10, delay_time=0)
    producer_b = Producer(char="B", repetitions=10, delay_time=1)
    producer_a.start()
    producer_b.start()
    producer_a.join()
    producer_b.terminate()

    # Computador de bicicleta
    bike_computer = BikeComputer()
    bike_computer.start()

if __name__ == "__main__":
    main()
