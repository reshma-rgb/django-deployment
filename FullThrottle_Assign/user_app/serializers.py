from rest_framework import serializers
from user_app.models import Profile,Activity,Member


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('start_time','end_time')

    def create(self, validated_data):
        subject = Activity.objects.create(start_time=validated_data['start_time'],end_time=validated_data['end_time'])
        return Activity

class ProfileSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many = True, read_only=True)
    class Meta:
        model = Profile
        fields = ('id','real_name', 'timezone','activity_periods')

    def create(self, validated_data):
        subject = Profile.objects.create(id=validated_data['id'],real_name=validated_data['real_name'],timezone=validated_data['timezone'],activity_periods=validated_data['activity_periods'])
        return Profile


class MemberSerializer(serializers.ModelSerializer):
    members = ProfileSerializer(many = True, read_only=True)
    class Meta:
        model = Member
        fields = ('okay','members')
