DEFAULT=/etc/default/fluentd

if [ -r $DEFAULT ]; then
    set -o allexport
    . $DEFAULT
    set +o allexport
fi

if [ "${1#-}" != "$1" ]; then
    set -- fluentd "$@"
fi

if [ "$1" = "fluentd" ]; then
    if ! echo $@ | grep -e ' \-c' -e ' \-\-config' ; then
       set -- "$@" --config /fluentd/etc/${FLUENTD_CONF}
    fi

    if ! echo $@ | grep -e ' \-p' -e ' \-\-plugin' ; then
       set -- "$@" --plugin /fluentd/plugins
    fi
fi

exec "$@"
