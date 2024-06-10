from collections.abc import Callable
from dataclasses import dataclass
from random import randint, uniform
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydistsim.network.network import NetworkType


@dataclass(slots=True, frozen=True)
class CommunicationPropertiesModel:
    "Communication properties for a network."

    message_ordering: bool  # if messages should be ordered (i.e. FIFO)
    message_delay_indicator: Callable[["NetworkType"], int]  # amount of steps to delay a given message
    message_loss_indicator: Callable[["NetworkType"], bool]  # if a message should be lost


#### Delay functions ####


def delay_size_network(network: "NetworkType") -> int:
    "Delay every message by the number of nodes in the network."
    return len(network.nodes)


def random_delay_max_size_network(network: "NetworkType") -> int:
    "Delay a message by a random number between 0 and the number of nodes in the network."
    return randint(0, len(network.nodes))


def do_not_delay(network: "NetworkType") -> int:
    "Do not delay any message."
    return 0


def delay_based_on_network_usage(network: "NetworkType") -> int:
    "Delay a message by the number of pending messages in the network."
    # 30 messages in a 10 node network == 3 steps delay
    return round(sum(len(node.outbox) for node in network.nodes) / len(network.nodes))


#### Loss functions ####


def random_loss(probability_of_loss) -> Callable[["NetworkType"], bool]:
    "Randomly lose a message with a given probability."

    def _random_loss(network: "NetworkType") -> bool:
        return uniform(0, 1) < probability_of_loss

    return _random_loss


def no_loss(network: "NetworkType") -> bool:
    "Do not lose any message."
    return False


#### Communication properties instances ####

# Properties for a network with message ordering, no message loss, and no message delay
IdealCommunication = CommunicationPropertiesModel(
    message_ordering=True,
    message_delay_indicator=do_not_delay,
    message_loss_indicator=no_loss,
)

# Properties for a network with no message ordering, no message loss, and no message delay
UnorderedCommunication = CommunicationPropertiesModel(
    message_ordering=False,
    message_delay_indicator=do_not_delay,
    message_loss_indicator=no_loss,
)

# Properties for a network with message ordering, no message loss, and a delay based on network usage
ThrottledCommunication = CommunicationPropertiesModel(
    message_ordering=True,
    message_delay_indicator=delay_based_on_network_usage,
    message_loss_indicator=no_loss,
)

# Properties for a network with no message ordering, no message loss, and a delay based on network usage
UnorderedThrottledCommunication = CommunicationPropertiesModel(
    message_ordering=False,
    message_delay_indicator=delay_based_on_network_usage,
    message_loss_indicator=no_loss,
)

# Properties for a network with message ordering, no message loss, and a random delay based on the network size
RandomDelayCommunication = CommunicationPropertiesModel(
    message_ordering=True,
    message_delay_indicator=random_delay_max_size_network,
    message_loss_indicator=no_loss,
)

# Properties for a network with no message ordering, no message loss, and a random delay based on the network size
UnorderedRandomDelayCommunication = CommunicationPropertiesModel(
    message_ordering=False,
    message_delay_indicator=random_delay_max_size_network,
    message_loss_indicator=no_loss,
)

# Properties for a network with message ordering, a random (but unlikely) message loss, and no message delay
UnlikelyRandomLossCommunication = CommunicationPropertiesModel(
    message_ordering=True,
    message_delay_indicator=do_not_delay,
    message_loss_indicator=random_loss(0.1),
)

# Properties for a network with message ordering, a random (but likely) message loss, and no message delay
LikelyRandomLossCommunication = CommunicationPropertiesModel(
    message_ordering=True,
    message_delay_indicator=do_not_delay,
    message_loss_indicator=random_loss(0.9),
)
