import grpc
import service_pb2
import service_pb2_grpc

# Connect to the gRPC server
channel = grpc.insecure_channel("localhost:80")
stub = service_pb2_grpc.MyServiceStub(channel)

# Call a method
response = stub.MyMethod(service_pb2.MyRequest(message="Me"))
print(response.message)
