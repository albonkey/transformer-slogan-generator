import React, { useEffect, useState } from 'react';
import { View, FlatList, StyleSheet } from 'react-native';

import { db, auth } from '../database/database';
import SloganItem from './SloganItem';  // Ensure the correct path to SloganItem component

const HistoryScreen = () => {
  const [slogans, setSlogans] = useState([]);

  useEffect(() => {
    const fetchSlogans = async () => {
      const user = auth.currentUser;
      if (!user) {
        console.log("No user is currently signed in.");
        return;
      }

      const snapshot = await db.collection(user.email).get();
      console.log(snapshot);

if (!snapshot.empty) {
  const slogansData = [];
  snapshot.forEach((doc) => {
    slogansData.push(doc.data());
  });
  setSlogans(slogansData);
} else {
  console.log("No documents found!");
}
    };

    fetchSlogans();
  }, []);

  return (
    <View style={styles.container}>
      <FlatList
        data={slogans}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => <SloganItem item={item} />}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#fff',
  }
});

export default HistoryScreen;
