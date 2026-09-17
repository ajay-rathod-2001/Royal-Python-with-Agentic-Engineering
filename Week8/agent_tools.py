from abc import ABC, abstractmethod



class Tool(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod

    def run(self, *args):
        ...



class CalculatorTool(Tool):

    def __init__(self):
        super().__init__("Calculator", "A tool for adding and multiplying numbers....!")
    
    def add(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def run(self, *args):
        a, b, name = args   ## 1,3,  "data"

        if name == "add":
            return self.add(a,b)
        elif name == "mul":
            return self.multiplication(a, b)
        else:
            raise ValueError(f"invalid Operation : {name}") 

class GreeterTool(Tool):

    def __init__(self):
        super().__init__("Greeter", "A tool for greeting people....!")

    def run(self, *args):
        name = args[0]
        return f"Hello, {name}!"


class Agent:
    def __init__(self, name):
        self.name = name
        self.tools = []  # [CalculatorTool, GreeterTool]

    def add_tool(self, tool:Tool):
        self.tools.append(tool)  # [CalculatorTool, GreeterTool]

    def list_tool(self):
        for tool in self.tools:
            print(f"{tool.name}, {tool.description}")  ## CalculatorTool().name, GreeterTool().description

    def use_tool(self, tool_name:str, *args):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.run(*args)

        return f"Tool {tool_name} is Not Found...!"


agent = Agent("My First Agent")

agent.add_tool(CalculatorTool())
agent.add_tool(GreeterTool())

agent.list_tool()

add_result = agent.use_tool("Calculator", 5, 7, "add")
mul_result = agent.use_tool("Calculator", 5, 7, "mul")

greet_result = agent.use_tool("Greeter", "Agentic Master")


print("Adding Result: ", add_result)
print("Multiplication Result: ", mul_result)
print("Greeting Result: ", greet_result)


