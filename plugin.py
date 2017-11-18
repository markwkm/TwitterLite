###
# Copyright (c) 2017, Mark Wong
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('TwitterLite')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

import twitter


class TwitterLite(callbacks.Plugin):
    """Twitter plugin just to retrieve tweets by screen name."""

    def __init__(self, irc):
        self.__parent = super(TwitterLite, self)
        self.__parent.__init__(irc)
        self.api = twitter.Api(consumer_key=self.registryValue('consumer_key'),
                  consumer_secret=self.registryValue('consumer_secret'),
                  access_token_key=self.registryValue('access_token_key'),
                  access_token_secret=self.registryValue('access_token_secret'))

    def t(self, irc, msg, args, screen_name):
        """<screen_name>

        Get the latest tweet from <screen_name>
        """
        try:
            tweet = self.api.GetUserTimeline(screen_name=screen_name, count=1)
            irc.reply(tweet[0].text, False)
        except Exception:
            irc.reply('Sorry, cannot get tweet from %s.' % screen_name)

    t = wrap(t, ['text'])


Class = TwitterLite


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
