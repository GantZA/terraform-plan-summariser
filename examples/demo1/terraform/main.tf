terraform {
  required_providers {
    mock = {
      source = "liamcervante/mock"
      version = "0.2.0"
    }
  }

  backend "local" {}
}

provider "mock" {
}

resource "mock_complex_resource" "ec2_cluster" {
  object = {
    bool = true
  }

  list_block {
    string = "hello world"
  }
}

resource "mock_simple_resource" "databricks_cluster" {
  string = "hello world 2"
}

resource "mock_simple_resource" "ssm_parameter" {
  integer = 2
}

resource "mock_simple_resource" "iam_rol" {
  integer = 100
}