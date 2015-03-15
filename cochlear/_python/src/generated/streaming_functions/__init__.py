RDT_PARSER_VERSION = '1.0.0'

FILES = ['streaming_interfering.c',
     'streamer.c',
     'streaming_frames_impl.c',
     'streaming_pairing.c',
     'streaming_timer.c',
     'streaming_nordic.c',
     'streaming_task_impl.c',
     'streaming_init_impl.c',
     'streaming_tools.c']

LINKER = 'ARM Linker, RVCT4.0 [Build 728]'

DATA_FILE = 'data.hex'

RESERVED_REGIONS = [(2164301824L, 4128), (2145395712, 4376), (2145400088, 400), (2145400488, 244)]

fw_crc_field = 0xe7dd

FWVERSION = 'galileo-vm.wroclaw.s3group.com:1666//cochlear/wav2/cr200ff_main.br/...@17394'

VERSION = 'galileo-vm.wroclaw.s3group.com:1666@17448'

COMPILER = 'ARM C/C++ Compiler, RVCT4.0 [Build 728]'

