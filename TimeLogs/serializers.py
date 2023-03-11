from  rest_framework import serializers

class TimelogSerializer(serializers.Serializer):

    team = serializers.CharField(max_length=250)
    username = serializers.CharField(max_length=250)
    job_number = serializers.CharField(max_length=250)
    booking_codes = serializers.CharField(max_length=250)
    booking_date = serializers.DateField()
    time_tracked = serializers.DecimalField(max_digits=5, decimal_places=1)
    task_estimate = serializers.DecimalField(max_digits=5, decimal_places=1)

