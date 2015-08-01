import unittest
import tempfile
import os
import sys

# Import caffe, maybe system path is needed

import caffe

class Action_Context_Layer(caffe.layer):
  """Layer for extract deep action contextual feature"""

  def setup(self, bottom, top):
    raise NotImplementedError("Set up function is still not implemented")


  def reshape(self, bottom, top):
    raise NotImplementedError("Reshape function is still not implemented")

  def forward(self, bottom, top):
    raise NotImplementedError("Forward function is still not implemented")

  def backward(self, bottom, top):
    raise NotImplementedError("Backward function is still not implemented")

class TestActionContextLayer(unittest.Testcase):
  def setup(self):
    raise NotImplementedError("Set up function is still not implemented")

  def test_reshape(self):
    raise NotImplementedError("Test reshape function is still not implemented")

  def test_forward(self, bottom, top):
    raise NotImplementedError("Test forward function is still not implemented")

  def test_backward(self, bottom, top):
    raise NotImplementedError("Test backward function is still not implemented")
