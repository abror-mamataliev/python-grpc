import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2


# Implement the gRPC service
class MyService(service_pb2_grpc.MyServiceServicer):
    def MyMethod(self, request, context):
        print(f"Received: {request.message}")
        return service_pb2.MyResponse(message=f"Hello, {request.message}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port("[::]:5000")
    print("Starting server on port 5000...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
