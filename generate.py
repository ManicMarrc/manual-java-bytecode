#!/usr/bin/python

if __name__ == '__main__':
    with open('HelloWorld.class', 'wb') as f:
        f.write(bytes([0xca, 0xfe, 0xba, 0xbe]))   # magic
        f.write(bytes([0x00, 0x00]))               # minor_version: 0
        f.write(bytes([0x00, 0x37]))               # major_version: 55

        f.write(bytes([0x00, 0x16]))               # constant_pool_count: 22
        # constant_pool start

        f.write(bytes([
            0x07,        # tag: CONSTANT_Class
            0x00, 0x02,  # name_index: 2
        ]))
        f.write(bytes([
            0x01,            # tag: CONSTANT_Utf8
            0x00, 0x0a,      # length: 10
            *b'HelloWorld'   # bytes: 'HelloWorld'
        ]))

        f.write(bytes([
            0x07,        # tag: CONSTANT_Class
            0x00, 0x04,  # name_index: 4
        ]))
        f.write(bytes([
            0x01,                 # tag: CONSTANT_Utf8
            0x00, 0x10,           # length: 16
            *b'java/lang/Object'  # bytes: 'java/lang/Object'
        ]))

        f.write(bytes([
            0x01,        # tag: CONSTANT_Utf8
            0x00, 0x04,  # length: 4
            *b'main'     # bytes: 'main'
        ]))
        f.write(bytes([
            0x01,                       # tag: CONSTANT_Utf8
            0x00, 0x16,                 # length: 22
            *b'([Ljava/lang/String;)V'  # bytes: '([Ljava/lang/String;)V'
        ]))

        f.write(bytes([
            0x01,        # tag: CONSTANT_Utf8
            0x00, 0x04,  # length: 4
            *b'Code'     # bytes: 'Code'
        ]))

        f.write(bytes([
            0x08,        # tag: CONSTANT_String
            0x00, 0x09,  # name_index: 9
        ]))
        f.write(bytes([
            0x01,              # tag: CONSTANT_Utf8
            0x00, 0x0d,        # length: 13
            *b'Hello, World!'  # bytes: 'Hello, World!'
        ]))

        f.write(bytes([
            0x09,        # tag: CONSTANT_Fieldref
            0x00, 0x0b,  # class_index: 11
            0x00, 0x0d,  # name_and_type_index: 13
        ]))
        f.write(bytes([
            0x07,        # tag: CONSTANT_Class
            0x00, 0x0c,  # name_index: 12
        ]))
        f.write(bytes([
            0x01,                 # tag: CONSTANT_Utf8
            0x00, 0x10,           # length: 16
            *b'java/lang/System'  # bytes: 'java/lang/System'
        ]))
        f.write(bytes([
            0x0c,        # tag: CONSTANT_NameAndType
            0x00, 0x0e,  # name_index: 14
            0x00, 0x0f,  # descriptor_index: 15
        ]))
        f.write(bytes([
            0x01,        # tag: CONSTANT_Utf8
            0x00, 0x03,  # length: 3
            *b'out'      # bytes: 'out'
        ]))
        f.write(bytes([
            0x01,                      # tag: CONSTANT_Utf8
            0x00, 0x15,                # length: 21
            *b'Ljava/io/PrintStream;'  # bytes: 'Ljava/io/PrintStream;'
        ]))

        f.write(bytes([
            0x0a,        # tag: CONSTANT_Methodref
            0x00, 0x11,  # class_index: 17
            0x00, 0x13,  # name_and_type_index: 19
        ]))
        f.write(bytes([
            0x07,        # tag: CONSTANT_Class
            0x00, 0x12,  # name_index: 18
        ]))
        f.write(bytes([
            0x01,                    # tag: CONSTANT_Utf8
            0x00, 0x13,              # length: 19
            *b'java/io/PrintStream'  # bytes: 'java/io/PrintStream'
        ]))
        f.write(bytes([
            0x0c,        # tag: CONSTANT_NameAndType
            0x00, 0x14,  # name_index: 20
            0x00, 0x15,  # descriptor_index: 21
        ]))
        f.write(bytes([
            0x01,        # tag: CONSTANT_Utf8
            0x00, 0x07,  # length: 7
            *b'println'  # bytes: 'println'
        ]))
        f.write(bytes([
            0x01,                      # tag: CONSTANT_Utf8
            0x00, 0x15,                # length: 21
            *b'(Ljava/lang/String;)V'  # bytes: '(Ljava/lang/String;)V'
        ]))

        # constant_pool end

        f.write(bytes([0x00, 0x21]))  # access_flags: ACC_PUBLIC | ACC_SUPER
        f.write(bytes([0x00, 0x01]))  # this_class: 1
        f.write(bytes([0x00, 0x03]))  # super_class: 3

        f.write(bytes([0x00, 0x00]))  # interfaces_count: 0
        # interfaces start
        # interfaces end

        f.write(bytes([0x00, 0x00]))  # fields_count: 0
        # fields start
        # fields end

        f.write(bytes([0x00, 0x01]))  # methods_count: 1
        # methods start

        f.write(bytes([
            0x00, 0x09,  # access_flags: ACC_PUBLIC | ACC_STATIC
            0x00, 0x05,  # name_index: 5
            0x00, 0x06,  # descriptor_index: 6
        ]))
        f.write(bytes([0x00, 0x01]))  # attributes_count: 1
        # attributes start

        f.write(bytes([
            0x00, 0x07,  # attributes_name_index: 7
            0x00, 0x00, 0x00, 0x15,  # attributes_length: 21
            0x00, 0x02,  # max_stack: 2
            0x00, 0x02,  # max_locals: 2
        ]))
        f.write(bytes([0x00, 0x00, 0x00, 0x09]))  # code_length: 9
        # code start

        f.write(bytes([
            0xb2, 0x00, 0x0a,  # getstatic 10
            0x12, 0x08,        # ldc 8
            0xb6, 0x00, 0x10,  # invokevirtual 16
            0xb1,              # return
        ]))

        # code end
        f.write(bytes([0x00, 0x00]))  # exception_table_length: 0
        # exception_table start
        # exception_table end
        f.write(bytes([0x00, 0x00]))  # attributes_count: 0
        # attributes start
        # attributes end

        # attributes end

        # methods end

        f.write(bytes([0x00, 0x00]))  # attributes_count: 0
        # attributes start
        # attributes end
