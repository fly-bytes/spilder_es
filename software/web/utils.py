import copy
import struct


class File_Type:
    def typeList(self, types):
        type_dict = {'jpg': ['FFD8FF'],
                     'png': ['89504E47'],
                     'gif': ['47494638396126026F01'],
                     'tif': ['49492A', '4D4D'],
                     'bmp': ['424D8E1B030000000000'],

                     'html': ['3C21444F435459504520'],
                     'htm': ['3C21646F637479706520'],
                     'css': ['48544D4C207B0D0A0942'],
                     'js': ['696B2E71623D696B2E71'],
                     'rtf': ['7B5C727466315C616E73'],

                     'eml': ['46726F6D3A203D3F6762'],
                     'wps': ['D0CF11E0A1B11AE10000'],
                     'mdb': ['5374616E64617264204A'],
                     'ps': '[252150532D41646F6265]',

                     'pdf': ['255044462D312E'],
                     'rmvb': ['2E524D46000000120001'],
                     'flv': ['464C5601050000000900'],
                     'mp4': ['00000020667479706D70'],
                     'mpg': ['000001BA210001000180'],

                     'wmv': ['3026B2758E66CF11A6D9'],
                     'wav': ['52494646E27807005741'],
                     'avi': ['52494646D07D60074156'],
                     'mid': ['4D546864000000060001'],

                     'zip': ['504B0304140000000800', '504B0304140000080800', '504B03040A0000080000'],
                     'rar': ['526172211A0700CF9073'],
                     'ini': ['235468697320636F6E66'],
                     'jar': ['504B03040A0000000000'],
                     'exe': ['4D5A9000030000000400'],
                     'jsp': ['3C25402070616765206C'],
                     'mf': ['4D616E69666573742D56'],

                     'xml': ['3C3F786D6C2076657273'],
                     'sql': ['494E5345525420494E54'],
                     'java': ['7061636B616765207765'],
                     'bat': ['406563686F206F66660D'],
                     'gz': ['1F8B0800000000000000'],

                     'properties': ['6C6F67346A2E726F6F74'],
                     'class': ['CAFEBABE0000002E0041'],
                     'docx': ['504B0304140006000800', '504B03040A0000000000'],
                     'torrent': ['6431303A637265617465'],

                     'mov': ['6D6F6F76'],
                     'wpd': ['FF575043'],
                     'dbx': ['CFAD12FEC5FD746F'],
                     'pst': ['2142444E'],
                     'qdf': ['AC9EBD8F'],
                     'pwl': ['E3828596'],
                     'ram': ['2E7261FD']
                     }
        ret = {}
        for k_hex, v_prefix in type_dict.items():
            if k_hex in types:
                ret[k_hex] = v_prefix
        return ret

    def bytes2hex(self, bytes):
        num = len(bytes)
        hexstr = u""
        for i in range(num):
            t = u"%x" % bytes[i]
            if len(t) % 2:
                hexstr += u""
            hexstr += t
        return hexstr.upper()

    def stream_type(self, stream, types):

        tl = self.typeList(types=types)
        ftype = None
        for type_name, hcode_list in tl.items():
            flag = False
            for hcode in hcode_list:
                numOfBytes = int(len(hcode) / 2)
                hbytes = struct.unpack_from("B" * numOfBytes, stream[0:numOfBytes])
                s_hcode = self.bytes2hex(hbytes)
                print("转成十六进制的编码", s_hcode, '=', "头文件", hcode, type_name)
                if s_hcode == hcode:
                    flag = True
                    break
            if flag:
                ftype = type_name
                break
        return ftype


if __name__ == '__main__':
    pass
