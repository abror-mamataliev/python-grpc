import grpc
import service_pb2_grpc
import service_pb2


def run():
    # Connect to the server
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)

        # Make a request
        response = stub.MyMethod(service_pb2.MyRequest(message="World"))
        print(f"Response: {response.message}")


if __name__ == "__main__":
    run()
