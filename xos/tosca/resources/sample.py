from xosresource import XOSResource
from service import XOSService
from services.vtr.models import SampleService


class ToscaSampleService(XOSService):
    provides = "tosca.nodes.Service"
    xos_model = SampleService
    copyin_props = [
      "description",
      "kind",
      "versionNumber",
      "public_key",
      "private_key_fn",
      "service_specific_id"
    ]


class ToscaSampleTenant(XOSResource):
    provides = "tosca.nodes.Tenant"
    xos_model = SampleTenant
