import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView,SafeAreaView, KeyboardAvoidingView, Platform, TouchableWithoutFeedback, Keyboard } from 'react-native';
import { getAuth } from 'firebase/auth';
import { getFirestore, doc, setDoc } from 'firebase/firestore';
import FormInput from '../components/FormInput';  // Ensure these are correctly imported
import { PrimaryButton } from '../components/Button';
import { TextInput } from 'react-native-paper';
const ProfileScreen = () => {
  const [userInfo, setUserInfo] = useState({
    name: '',
    email: '',
    phone: ''
  });

  useEffect(() => {
    const auth = getAuth();
    const user = auth.currentUser;
    if (user) {
      setUserInfo({
        name: user.displayName || '',
        email: user.email,
        phone: user.phoneNumber || 'No phone number set'
      });
    }
  }, []);

  const handleUpdate = async () => {
    const db = getFirestore();
    const userDoc = doc(db, 'userdata', userInfo.email.replace(/\./g, ',')); // Sanitize email as document ID
    await setDoc(userDoc, userInfo, { merge: true });
    alert('Profile updated successfully!');
  };

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        keyboardVerticalOffset={Platform.OS === "ios" ? 64 : 0}
      >
        <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
          <ScrollView>
            <View style={{ alignItems: 'center', marginVertical: 60 }}>
              <Text style={styles.title}>Update Profile</Text>
            
              <FormInput
                label="Name"
                
                value={userInfo.name}
                onChange={(text) => setUserInfo({ ...userInfo, name: text })}
                containerStyle={styles.input}
              />

              <FormInput
                label="Email (non-editable)"
                value={userInfo.email}
                editable={false}
                containerStyle={styles.input}
              />

              <FormInput
                label="Phone Number"
                value={userInfo.phone}
                onChangeText={(text) => setUserInfo({ ...userInfo, phone: text })}
                containerStyle={styles.input}
              />

              <PrimaryButton
                btnContainer={styles.button}
                title="Save Changes"
                onPress={handleUpdate}
              />
            </View>
          </ScrollView>
        </TouchableWithoutFeedback>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '100%',
    marginBottom: 10,
    
  },
  button: {
    backgroundColor: 'dodgerblue',
    height: 55,
    width: 200,
    borderRadius: 24,
    marginTop: 20,
  },
});

export default ProfileScreen;
