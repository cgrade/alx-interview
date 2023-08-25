def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Initialize a variable to keep track of the expected number of c
    # ontinuation bytes
    expected_continuation_bytes = 0

    # Iterate through each integer in the data list
    for byte in data:
        # Check if this byte is a continuation byte
        if expected_continuation_bytes > 0:
            # If it is, it should start with '10'
            if not is_continuation(byte):
                return False
            expected_continuation_bytes -= 1
        else:
            # Determine the number of leading '1' bits in the byte
            mask = 0b10000000
            while (byte & mask):
                expected_continuation_bytes += 1
                mask >>= 1

            # If it's a single-byte character (starts with '0' or no l
            # eading '1' bits), no continuation bytes are expected
            if expected_continuation_bytes == 0:
                continue

            # Check if the number of expected continuation byte
            # is within the valid range
            if expected_continuation_bytes \
               < 1 or expected_continuation_bytes > 3:
                return False

    # After processing all bytes, if there are still expected continuation
    # bytes, it's not a valid encoding
    return expected_continuation_bytes == 0
