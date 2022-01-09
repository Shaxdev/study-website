from django.core.exceptions import ValidationError
# import magic
# def validate_mime_type(value):
#     supported_types=['application/pdf',]
#     with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
#         mime_type=m.id_buffer(value.file.read(1024))
#         value.file.seek(0)
#     if mime_type not in supported_types:
#         raise ValidationError(u'Unsupported file type.')
    
    
    
def document_validate_file_extension(value):
    """ Bu extention .pdf, .doc, .docx larni qo'llab quvvatlaydi"""
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf','.doc','.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')
    
def prezintatsiya_validate_file_extension(value):
    """ Bu extention .ppt, .pptx larni qo'llab quvvatlaydi"""
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.ppt','.pptx']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')
    
def video_validate_file_extension(value):
    """ Bu extention .ppt, .pptx larni qo'llab quvvatlaydi"""
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')