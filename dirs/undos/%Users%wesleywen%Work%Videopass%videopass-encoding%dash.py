Vim�UnDo� +��x����K�V���%�&��2��Q3T�D�H ;  �                                  TQ�   	 _�                    w       ����                                                                                                                                                                                                                                                                                                                                                             TGQ�     �  v  x  �      L    #TODO: Assume segments are in sub-folder with the same namebase as .mpd.5�_�                    F        ����                                                                                                                                                                                                                                                                                                                                                             TGQ�    �   �   �          /    '''Patch trun and saio box in a .mp4 file. �   E   G              5�_�                   x   ,    ����                                                                                                                                                                                                                                                                                                                                                             TGQ�    �  w  y  �      C    seg_dirpath = mpd_filepath.splitext()[0] # no slash at the end.5�_�                   z   +    ����                                                                                                                                                                                                                                                                                                                                                             TGQ�     �  z  |  �      l                             s3_bucket, root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file�  y  |  �      z    s3.upload_big_file_to_s3(mpd_filepath, s3_bucket, root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file5�_�                   {   )    ����                                                                                                                                                                                                                                                                                                                                                             TGQ�     �  z  |  �      l                             s3_bucket, root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file5�_�                   {   (    ����                                                                                                                                                                                                                                                                                                                                                             TGQ�     �  {  }  �      a                             root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file�  z  }  �      l                             s3_bucket, root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file5�_�                   |   4    ����                                                                                                                                                                                                                                                                                                                                                             TGQ�     �  {  }  �      a                             root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file5�_�      	             |   L    ����                                                                                                                                                                                                                                                                                                                           |   L      |   `       v   `    TGQ�     �  {  }  �      a                             root_s3_key.joinpath(mpd_filepath.basename())) #TODO: not a big file5�_�      
           	  y   *    ����                                                                                                                                                                                                                                                                                                                           |   L      |   `       v   `    TGQ�     �  y  {  �    5�_�   	              
  z        ����                                                                                                                                                                                                                                                                                                                           }   L      }   `       v   `    TGQ�     �  y  {  �       �  z  {  �    5�_�   
                z        ����                                                                                                                                                                                                                                                                                                                           }   L      }   `       v   `    TGQ�     �  y  {  �      #TODO: not a big file5�_�                   z       ����                                                                                                                                                                                                                                                                                                                           }   L      }   `       v   `    TGQ�     �  y  {  �          #TODO: not a big file5�_�                   {        ����                                                                                                                                                                                                                                                                                                                           }   L      }   `       v   `    TGQ�    �  |  ~          L                             root_s3_key.joinpath(mpd_filepath.basename())) �  {  }          (                             s3_bucket, �  z  |          +    s3.upload_big_file_to_s3(mpd_filepath, 5�_�                   z       ����                                                                                                                                                                                                                                                                                                                                                             TQ�      �  y  z              # TODO: not a big file5�_�                   z       ����                                                                                                                                                                                                                                                                                                                                                             TQ�%     �  y  {  �      *    s3.upload_big_file_to_s3(mpd_filepath,5�_�                   z       ����                                                                                                                                                                                                                                                                                                                                                             TQ�)     �  y  {  �          s3.upload_(mpd_filepath,5�_�                   {       ����                                                                                                                                                                                                                                                                                                                                                             TQ�/     �  z  |  �      '                             s3_bucket,5�_�                   |       ����                                                                                                                                                                                                                                                                                                                                                             TQ�0    �  {  }  �      K                             root_s3_key.joinpath(mpd_filepath.basename()))5�_�                   y   ;    ����                                                                                                                                                                                                                                                                                                                                                             TQ��     �  x  z  �      <    s3.upload_dir_to_s3(seg_dirpath, s3_bucket, root_s3_key)5�_�                   y   D    ����                                                                                                                                                                                                                                                                                                                                                             TQ��     �  x  z  �      E    s3.upload_dir_to_s3(seg_dirpath, s3_bucket, root_s3_key.joinpath)5�_�                   y   Z    ����                                                                                                                                                                                                                                                                                                                                                             TQ�    �  x  z  �      \    s3.upload_dir_to_s3(seg_dirpath, s3_bucket, root_s3_key.joinpath(mpd_filepath.namebase))5�_�                   y   %    ����                                                                                                                                                                                                                                                                                                                                                             TQ�	     �  y  {  �      O                        s3_bucket, root_s3_key.joinpath(mpd_filepath.namebase))�  x  {  �      \    s3.upload_dir_to_s3(seg_dirpath, s3_bucket, root_s3_key.joinpath(mpd_filepath.namebase))5�_�                   z       ����                                                                                                                                                                                                                                                                                                                                                             TQ�     �  y  {  �      O                        s3_bucket, root_s3_key.joinpath(mpd_filepath.namebase))5�_�                   z   #    ����                                                                                                                                                                                                                                                                                                                                                             TQ�     �  y  |  �      O                        s3_bucket, root_s3_key.joinpath(mpd_filepath.namebase))5�_�                    y        ����                                                                                                                                                                                                                                                                                                                                                             TQ�   	 �  y  {          #                        s3_bucket, �  x  z          %    s3.upload_dir_to_s3(seg_dirpath, 5��