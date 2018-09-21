from ipykernel.kernelapp import IPKernelApp
from .kernel import gfortKernel
IPKernelApp.launch_instance(kernel_class=gfortKernel)
