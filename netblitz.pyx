from libcpp.vector cimport vector
from libcpp.string cimport string


cdef extern from "netblitz_impl.cpp":
     cdef cppclass nbFile:
         nbFile(string) except +
         void vars()

cdef class File:
     cdef nbFile* cFile
     def __cinit__(self, name):
         self.cFile = new nbFile(<string>name.encode('utf-8'))

     def __dealloc__(self):
         del self.cFile

     def var(self):
         self.cFile.vars()
