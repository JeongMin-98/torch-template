import torch.utils.data
from .torch_model import DeepNetwork
from utils.dataLoader import ImageDataset
from utils.utils import *
from network.exampleNet import *
from torch.utils.tensorboard import SummaryWriter
from torchsummary import summary


def run_fn(args):
    device = check_device()
    model = myMnistNet(args)
    model.build_model(device)

    summary(model.network, (1, 28, 28), device="cuda")

    # model.train_model(device)


class myMnistNet(DeepNetwork):
    def __init__(self, args):
        super(DeepNetwork, self).__init__()
        self.model_name = "myMnistNet"  # will be able to custom model_name
        self.config_dir = args['config_dir']

        self.config_dir = os.path.join(self.config_dir, self.model_name)
        check_folder(self.config_dir)

        config_path = os.path.join(self.config_dir, self.model_name + ".cfg")
        self.cfg = parse_model_config(config_path)

        # 다음에 적용할 부분
        # self.config_dir = os.path.join(self.config_dir, self.model_dir)
        # check_folder(self.config_dir)

    def build_model(self, device):
        """ Load dataset"""
        # implement soon

        """ Network """
        self.network = Net(config=self.cfg).to(device)

        """ Optimizer """
        # implement soon

