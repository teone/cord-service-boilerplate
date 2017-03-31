# XPROTO Specified Models

xproto is a model definition language defined as part of XOS. It is derived from Google's Protobufs specification language, and extends Protubufs with some syntactically sugared extensions. xproto files can be converted into Protobufs, and vice versa, without loss in information. However, while in Protobufs XOS-specific features are expressed as anonymous options, in the xproto versions, those options are syntactically explicit. 

Any Protobuf file is an xproto file. So if you have a pre-written Protobuf specification of your model, then it can be used as is. In addition, models can be linked together with "links":

     required manytoone target_type->ContentType:vtrtenant = 17 [db_index = True, null = False, blank = False];

The above line specifies a link between the current model and the ContentType model. The field in the current model that stores the reference is target\_type, and the field in the peer model that contains the backreference is vtrtenant. The link is manytoone but could also be manytomany or onetoone.

Also, any message or field definition can be associated with a "policy":

     required string instance_id::feedback = 10;

"feedback" in the above line is a policy, which XOS internally interprets to mean that the field in question is populated by the back end.

In addition to links and policies, field options can take the following additional values:

* stripped (boolean): A string in which whitespaces are removed
* default (any type): The default value of the current field
* choices (tuple): The set of options that the field is allowed to take
* help\_text (string): A string describing the use of the field
* max\_length (int): The number of characters in a string
* blank (boolean): Signifies whether the field can be empty
* null (boolean): Signifies whether the field can be unset
* db\_index (boolean): Signifies whether the field is associated with a database index




