resource "aws_instance" "instance" {
  ami           = "ami-053b0d53c279acc90"
  instance_type = "t3.medium"
  tags = merge(local.common_tags, {
    Name = "Flasktice Instance for Testing"
  })
}