variable "aws_region" {
  type        = string
  description = "AWS Region to use for resources"
  default     = "us-east-1"
}

variable "company" {
  type        = string
  description = "Company name"
  default     = "AleksDeveloping"
}

variable "project" {
  type        = string
  description = "Project name"
  default     = "Flasktice"
}

variable "billing_code" {
    type        = string
    description = "Billin Code"
    default     = "XXAWWSD980902"
}