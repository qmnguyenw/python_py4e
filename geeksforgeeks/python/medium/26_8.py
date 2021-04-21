Data type Object (dtype) in NumPy Python



Every ndarray has an associated data type (dtype) object. This data type
object (dtype) informs us about the layout of the array. This means it gives
us information about :

  * Type of the data (integer, float, Python object etc.)
  * Size of the data (number of bytes)
  * Byte order of the data (little-endian or big-endian)
  * If the data type is a sub-array, what is its shape and data type.

The values of an ndarray are stored in a buffer which can be thought of as a
contiguous block of memory bytes. So how these bytes will be interpreted is
given by the dtype object.

