resource "aws_instance" "controlNode" {
  ami           = "ami-0360c520857e3138f"
  instance_type = "t2.micro"
  key_name      = "myserver"

  tags = {
    Name = "controlNode"
  }
}
resource "aws_instance" "managedNode1" {
  ami           = "ami-0360c520857e3138f"
  instance_type = "t2.micro"
  key_name      = "myserver"

  tags = {
    Name = "managedNode1"
  }
}

resource "aws_instance" "managedNode2" {
  ami           = "ami-0360c520857e3138f"
  instance_type = "t2.micro"
  key_name      = "myserver"

  tags = {
    Name = "managedNode2"
  }
}
{}
